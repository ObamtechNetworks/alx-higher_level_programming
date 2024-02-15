#!/usr/bin/node
// a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const data = require('./101-data').dict;

const userOccurrences = {};

// Iterate through the original dictionary and populate the new dictionary
Object.keys(data).forEach((userId) => {
  const occurrences = data[userId];

  if (!userOccurrences[occurrences]) {
    userOccurrences[occurrences] = [userId];
  } else {
    userOccurrences[occurrences].push(userId);
  }
});

console.log(userOccurrences);
