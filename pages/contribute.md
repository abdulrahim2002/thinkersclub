---
layout: page
menu: false
date: '2024-07-21 05:53:59'
title: Contribute
description: contributing
permalink: /contribute/
---

<img class="img-rounded" src="/assets/img/uploads/abdulrahim.png" alt="Thinkers Club logo" width="200">


# Contributions

To contribute to out website your need to clone this repo, add your post using `initpost.py` or manually adding your post in `_posts`. Please note the front matter properties. 

 
# test

```
<this will be invisible>
```


```java
public class HelloWorld {

    // Method to print a greeting message
    public void printGreeting(String name) {
        System.out.println("Hello, " + name + "!");
    }

    // Main method
    public static void main(String[] args) {
        // Create an instance of HelloWorld
        HelloWorld helloWorld = new HelloWorld();

        // Print greeting messages
        helloWorld.printGreeting("Alice");
        helloWorld.printGreeting("Bob");
        helloWorld.printGreeting("Charlie");

        // Sum of two numbers
        int a = 5;
        int b = 10;
        int sum = a + b;
        System.out.println("The sum of " + a + " and " + b + " is " + sum);

        // Check if a number is even or odd
        int number = 7;
        if (number % 2 == 0) {
            System.out.println(number + " is even.");
        } else {
            System.out.println(number + " is odd.");
        }
    }
}
```

# Here's C code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100
#define MAX_NAME_LENGTH 50

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    float grade;
} Student;

void addStudent(Student students[], int *count);
void displayStudents(const Student students[], int count);
void saveStudentsToFile(const Student students[], int count, const char *filename);
void loadStudentsFromFile(Student students[], int *count, const char *filename);

int main() {
    Student students[MAX_STUDENTS];
    int count = 0;
    int choice;

    while (1) {
        printf("\nStudent Management System\n");
        printf("1. Add Student\n");
        printf("2. Display Students\n");
        printf("3. Save Students to File\n");
        printf("4. Load Students from File\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addStudent(students, &count);
                break;
            case 2:
                displayStudents(students, count);
                break;
            case 3:
                saveStudentsToFile(students, count, "students.txt");
                break;
            case 4:
                loadStudentsFromFile(students, &count, "students.txt");
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
```

# R code

```r
# Load necessary libraries
library(ggplot2)
library(dplyr)

# Load the iris dataset
data(iris)

# Inspect the first few rows of the dataset
head(iris)

# Summary statistics of the dataset
summary(iris)

# Data manipulation using dplyr
# Calculate the mean sepal length for each species
mean_sepal_length <- iris %>%
  group_by(Species) %>%
  summarize(mean_sepal_length = mean(Sepal.Length))

# Print the result
print(mean_sepal_length)

# Plotting using ggplot2
# Scatter plot of Sepal.Length vs Sepal.Width colored by Species
ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(size = 3) +
  labs(title = "Sepal Length vs Sepal Width",
       x = "Sepal Length (cm)",
       y = "Sepal Width (cm)",
       color = "Species") +
  theme_minimal()

# Save the plot to a file
ggsave("scatter_plot.png", width = 8, height = 6)

```


here shell:

```bash
#!/bin/bash

# A simple script to back up a directory

# Define the source and destination directories
SOURCE_DIR="/path/to/source"
DEST_DIR="/path/to/destination"

# Get the current date and time for the backup folder name
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

# Create the backup directory
BACKUP_DIR="$DEST_DIR/backup_$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

# Copy the files
cp -r "$SOURCE_DIR/"* "$BACKUP_DIR/"

# Print a message indicating completion
echo "Backup of $SOURCE_DIR completed successfully at $BACKUP_DIR"
```

# yml

```yml
# YAML example: Configuration file for a web application

server:
  host: "localhost"
  port: 8080

database:
  type: "mysql"
  host: "db.example.com"
  port: 3306
  username: "dbuser"
  password: "dbpass"
  name: "mydatabase"

logging:
  level: "INFO"
  file: "/var/log/myapp.log"

features:
  authentication: true
  analytics: false
```