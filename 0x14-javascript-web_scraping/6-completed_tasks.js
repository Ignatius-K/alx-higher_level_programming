#!/usr/bin/node
/**
 * 6-completed_tasks
 * Written by Ignatius K <ignatiuskisekka@gmail.com>
 *
 * Script that computes number of tasks completed by user
 */

const { argv, exit } = require('node:process');
const request = require('request');

const NUM_OF_EXPECTED_ARGS = 3;
if (argv.length < NUM_OF_EXPECTED_ARGS) {
  console.error(`Usage: ${argv[1]} {url}`);
  exit(1);
}

const url = argv[2];
request(url, {}, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.info(`code: ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);
  const userTodoCount = {};

  todos.forEach(todo => {
    if (!todo.completed) return;
    if (!userTodoCount[todo.userId]) {
      userTodoCount[todo.userId] = 0;
    }
    userTodoCount[todo.userId]++;
  });

  console.log(userTodoCount);
});
