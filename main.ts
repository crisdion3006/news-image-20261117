// A working news-image-daily entry (Node 22, standard library only): its image
// is the entry.png beside this file, and the program copies it to
// /output/entry.png. The image sums up the world news of Tuesday 17 November
// 2026 in one 1024x1024 infographic: a big date header and six story panels
// (Kerch Bridge, Trump in Manila, Gulf tensions, Nvidia's Huang, US measles
// status, Japan's jets), drawn programmatically with real text so nothing
// garbles. The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by
// 1024 pixels, and the judge sees exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
