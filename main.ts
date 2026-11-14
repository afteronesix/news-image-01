// news-image-01 entry (Node 22, standard library only): copies the image
// beside this file to the output directory. The image sums up the world's
// news of Friday 13 November 2026: Senate summons Nvidia's chief, Zelensky
// meets US envoys, a drone hits a Russian warship, Iran strikes a US radar
// base in Bahrain, the FBI's $400m crypto heist, and Kane's 126th England
// cap, in a front-page montage with a globe at its centre.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

function resolveSource() {
  const here = new URL('./entry.png', import.meta.url);
  const fromScript = fileURLToPath(here);
  if (existsSync(fromScript)) return fromScript;
  const fromCwd = join(process.cwd(), 'entry.png');
  if (existsSync(fromCwd)) return fromCwd;
  throw new Error('entry.png not found beside main.ts or in the working directory');
}

const source = resolveSource();
const bytes = readFileSync(source);
if (!bytes.subarray(0, 8).equals(PNG_SIGNATURE)) {
  throw new Error('entry.png is not a PNG (bad 8-byte signature)');
}
if (bytes.length > 1048576) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB limit`);
}
// IHDR chunk: width and height are big-endian uint32 at offsets 16 and 20.
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 limit`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, 'entry.png');
copyFileSync(source, dest);
console.log(`wrote ${dest} (${statSync(dest).size} bytes, ${width}x${height})`);
