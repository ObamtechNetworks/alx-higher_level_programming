#!/usr/bin/node

// Import fileSystem
const fs = require('fs');

// Read CMD arguments
const arg = process.argv.slice(2);

const sourceFile1 = arg[0];
const sourceFile2 = arg[1];
const destinationFile = arg[2]; // Corrected index

// Array to store file contents
const finalFiles = [];

// Read from sourceFile1
fs.readFile(sourceFile1, 'utf8', (readErr, data1) => {
  if (readErr) {
    console.error(`Error reading from ${sourceFile1}:`, readErr);
    return;
  }

  // Read from sourceFile2
  fs.readFile(sourceFile2, 'utf8', (readErr, data2) => {
    if (readErr) {
      console.error(`Error reading from ${sourceFile2}:`, readErr);
      return;
    }

    // Concatenate both data to an array
    finalFiles.push(data1, data2);

    // Convert the array to a string
    const concatenatedContent = finalFiles.join('');

    // Write to output file
    fs.writeFile(destinationFile, concatenatedContent, 'utf8', (writeErr) => {
      if (writeErr) {
        console.error(`Error writing to ${destinationFile}:`, writeErr);
      }
    });
  });
});
