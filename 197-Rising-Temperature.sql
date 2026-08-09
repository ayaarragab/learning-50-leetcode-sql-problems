# Write your MySQL query statement below
SELECT today.id
FROM Weather AS today
INNER JOIN Weather AS yesterday
ON today.recordDate = DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY)
Where today.temperature > yesterday.temperature;