import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { dirname, extname, join, normalize, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const publicDirectory = resolve(scriptDirectory, '..', 'dist');
const preferredPort = Number(process.env.DEMO_PORT ?? 4173);

const mimeTypes = {
  '.css': 'text/css; charset=utf-8',
  '.geojson': 'application/geo+json; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
};

function safeFilePath(requestUrl) {
  const url = new URL(requestUrl ?? '/', 'http://localhost');
  const requestedPath = decodeURIComponent(url.pathname === '/' ? '/index.html' : url.pathname);
  const candidate = normalize(join(publicDirectory, requestedPath));
  return candidate.startsWith(publicDirectory) ? candidate : join(publicDirectory, 'index.html');
}

async function respondWithFile(response, filePath) {
  const body = await readFile(filePath);
  const extension = extname(filePath).toLowerCase();
  response.writeHead(200, {
    'Cache-Control': extension === '.html' ? 'no-cache' : 'public, max-age=3600',
    'Content-Type': mimeTypes[extension] ?? 'application/octet-stream',
  });
  response.end(body);
}

const server = createServer(async (request, response) => {
  try {
    const filePath = safeFilePath(request.url);
    const metadata = await stat(filePath).catch(() => null);

    if (metadata?.isFile()) {
      await respondWithFile(response, filePath);
      return;
    }

    await respondWithFile(response, join(publicDirectory, 'index.html'));
  } catch (error) {
    response.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
    response.end(`Demo tidak dapat dibuka: ${error instanceof Error ? error.message : 'galat tak dikenal'}`);
  }
});

function listen(port) {
  const handleError = (error) => {
    server.off('listening', handleListening);
    if (error.code === 'EADDRINUSE' && port < preferredPort + 20) {
      listen(port + 1);
      return;
    }
    throw error;
  };

  const handleListening = () => {
    server.off('error', handleError);
    const url = `http://127.0.0.1:${port}`;
    process.stdout.write(`\nMedan Relasional Jakarta\n${url}\nIlustrasi prototipe — bukan hasil penelitian.\n\nTekan Control+C untuk menutup server.\n`);

    if (process.platform === 'darwin' && process.env.NO_OPEN !== '1') {
      const opener = spawn('open', [url], { detached: true, stdio: 'ignore' });
      opener.unref();
    }
  };

  server.once('error', handleError);
  server.once('listening', handleListening);
  server.listen(port, '127.0.0.1');
}

listen(preferredPort);

process.on('SIGINT', () => {
  server.close(() => process.exit(0));
});
