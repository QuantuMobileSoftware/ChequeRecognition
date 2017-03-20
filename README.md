# ChequeRecognition

## Description

The aim of this project is to provide an ability to recognize checks on photos. Current version support russian language and working with cheques of that type.

## Techologies
* Python
* OpenCV
* OCR Tesseract

## Example

There is an `img.jpg` picture of regular bill in the repository. After code run recognized text is printed on the screen, where the following string can be seen:

`СУМА 440.00 ГРН`

which helps simply understand total sum of the bill is `440 UAH`.

## Usage

Current approach helps run project with docker-compose, so after [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/) installation only few commands should be run:

```
sudo docker-compose up
```
