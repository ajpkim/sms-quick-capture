# SMS Quick Capture

This project uses the Twilio API to enable quick capture via SMS of personal data for later processing.

# Message Formats

SMS message syntax is as follows (tags are optional).

```
<message_type>
<content...>
<#>
<tag1>
<tag2>
```

Newlines are used to parse the 3 message featues: message type, content, and tags.

## General Messages

General messages have no additional fields beyond `content`.

Here is an example (with a tag):

```
1
Remeber to finish watching game 6 of the 1984 NBA Finals this weekend
#
bball
```

## Expense Messages

Expense messages break up `content` into additional fields: `amount`, `category`, and `description`.

```
2
<amount>
<category>
<descriotion>
<#>
<tag1>
<tag2>
```

Here is an example (without tags):
```
2
10.45
food
coffee and scone from coffeeshop
```

# Error Messages

There is minimal error-checking, but if message processing fails in one of the covered ways, then an error message will be returned to sender.
