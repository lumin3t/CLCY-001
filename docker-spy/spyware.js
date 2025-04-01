const chokidar = require("chokidar");
const fsExtra = require("fs-extra");
const fs = require("fs");
const path = require("path");

const watchDir = "uploads";
const targetDir = "stolen";

// Ensure target directory exists
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir);
}

// Watch for new files
chokidar.watch(watchDir, { persistent: true }).on("add", (filePath) => {
  const fileName = path.basename(filePath);
  const newPath = path.join(targetDir, fileName);
  fsExtra.move(filePath, newPath, (err) => {
    if (err) console.error("Error moving file:", err);
    else console.log(`File stolen: ${fileName}`);
  });
});
