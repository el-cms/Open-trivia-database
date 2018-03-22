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
  "tags":["CATEGORY_NAME", "TAG1", "TAGN"],
  "answers": [
    "answer 0",
    "answer 1",
    "answer n",
  ],
  "source" : "http://example.com"
}
```

## Valid question
A question is considered "valid" when:
- It has more than 1 answers
- Have a "good" answer
- Have a link to the source (explanation of the answer)
- Have one or more tags

## Category and tags
What between categories and tags ?
- A question can have multiple tags
- The category is the tag that best defines the question.

Tags and category should be an ENGLISH_SINGULAR_UPPERCASED_STRING to be used as index
(for translations or whatever).

## File organisation
- All "todo" folders contain non-finished files.
- "need_review" folders contains questions with some answers but need validation
- Validated questions are in the language root folder:

```text
en:
  todo/            <- New questions
    history.json
  staging/         <- Incomplete questions with answers
    history.json
  history.json     <- Complete history questions
```

## Participating:
If you want to participate to this project, you're welcome. Please, follow these
simple guidlines:

  - A question should be written on ONE line only (we have big files here...)
  - New questions should be written at the end of the file.
  - New questions should have a source.
  - Take a good care about the text you write (typos, casing, etc... : no "Every Word In Uppercase" or other fancy styles)

## Special thanks:
Thanks to [007craft](https://www.reddit.com/user/007craft) who created the original database on [this reddit thread](https://www.reddit.com/r/trivia/comments/3wzpvt/free_database_of_50000_trivia_questions/).
