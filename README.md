## Synopsis

The aim of this project is to provide an ability to recognize checks.
Current version helps to parse russian bills.

## Example

There is an `img.jpg` picture of regular bill in the repository. After code run recognized text is printed on the screen, where the following string can be seen:

`СУМА 440.00 ГРН`

which helps simply understand total sum of the bill is `440 UAH`.

## Installation

Current approach helps run project with docker-compose, so after [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/) installation only few commands should be run:

```bash
git clone https://github.com/andrewdemchenkodeveloper/ChequeRecognition.git
cd ChequeRecognition
sudo docker-compose up
```

Enjoy!