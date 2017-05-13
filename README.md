# Open-trivia-database
Open database of questions and answers

## License
Facts are fact, we can't license that. If you use this work, please cite this
repository and add a link to it in your work.

## Format
All files correspond to a category. The files are lists of JSON objects like:

```json
{
  "category_id" : "CATEGORY NAME",
  "lang" : "en",
  "question" : "Question text",
  "answer" : 0,
  "answers": [
    "answer 0",
    "answer 1",
    "answer n",
  ],
  "source" : "http://example.com"
}
```

## File organisation
All "todo" folders contain non-finished files.

## Participating:
If you want to participate to this project, you're welcome. Please, follow these
simple guidlines:

  - A question should be written on ONE line only (we have big files here...)
  - New questions should be written at the end of the file.
  - New questions should have a source.
  - Take a good care about the text you write (typos, casing, etc... : no "Every Word In Uppercase" or other fancy styles)

## Special thanks:
Thanks to [007craft](https://www.reddit.com/user/007craft) who created the original database on [this reddit thread](https://www.reddit.com/r/trivia/comments/3wzpvt/free_database_of_50000_trivia_questions/).
