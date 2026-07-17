SELECT * FROM employees;

SELECT name, salary
FROM employees
WHERE salary > 50000;

SELECT department, COUNT(*)
FROM employees
GROUP BY department;

SELECT AVG(salary)
FROM employees;

SELECT SUM(salary)
FROM employees;

SELECT *
FROM employees
ORDER BY salary DESC;
