const fs = require("fs");

let maxCalories = 0;
let currentCalories = 0;

try {
  const fileContent = fs.readFileSync("../input.txt", "utf-8");
  fileContent.split(/\r?\n/).forEach((line) => {
    if (line !== "") {
      currentCalories += parseInt(line);
    } else {
      if (maxCalories < currentCalories) {
        maxCalories = currentCalories;
      }
      currentCalories = 0;
    }
  });
  console.log(maxCalories);
} catch (err) {
  console.error(err);
}
