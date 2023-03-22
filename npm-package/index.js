import fs from "fs";

function getOscarMatrix() {
  const data = fs.readFileSync("pbom_data/matrix.json", "utf8");
  return JSON.parse(data);
}

export default getOscarMatrix;
