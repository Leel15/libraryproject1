INSERT INTO bookmodule_book (id, title, price, quantity, pubdate, rating, publisher_id) VALUES 
(1, 'Clean Code', 150.0, 5, '2023-01-01 10:00:00', 5, 2),
(2, 'The Pragmatic Programmer', 180.0, 10, '2023-02-15 10:00:00', 4, 1),
(3, 'Grokking Algorithms', 120.0, 8, '2023-03-20 10:00:00', 5, 3),
(4, 'Domain-Driven Design', 200.0, 3, '2023-04-10 10:00:00', 4, 2),
(5, 'Refactoring', 160.0, 7, '2023-05-05 10:00:00', 3, 1),
(6, 'Design Patterns', 190.0, 2, '2023-06-18 10:00:00', 5, 2),
(7, 'Test Driven Development', 140.0, 4, '2023-07-22 10:00:00', 4, 3),
(8, 'Working Effectively with Legacy Code', 170.0, 6, '2023-08-30 10:00:00', 3, 1),
(9, 'The Clean Coder', 130.0, 12, '2023-09-12 10:00:00', 5, 2),
(10, 'Introduction to Algorithms', 250.0, 1, '2023-10-01 10:00:00', 5, 1);

INSERT INTO bookmodule_author (id, name, DOB) VALUES 
(1, 'Robert C. Martin', '1952-12-05'),
(2, 'Andrew Hunt', '1964-10-20'),
(3, 'Aditya Bhargava', '1988-05-15'),
(4, 'Eric Evans', '1970-03-12');

INSERT INTO bookmodule_publisher (id, name, location) VALUES 
(1, 'O Reilly Media', 'California, USA'),
(2, 'Pearson Education', 'London, UK'),
(3, 'Manning Publications', 'New York, USA');

INSERT INTO bookmodule_book_authors (book_id, author_id) VALUES 
(1, 1), (2, 2), (3, 3), (4, 4), (5, 1), 
(6, 4), (7, 2), (8, 1), (9, 1), (10, 3);