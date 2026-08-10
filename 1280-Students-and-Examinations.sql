# Write your MySQL query statement below
SELECT S.student_id, S.student_name, SU.subject_name, COUNT(E.subject_name) AS attended_exams
FROM Students AS S
CROSS JOIN SUBJECTS AS SU
LEFT JOIN Examinations AS E
ON SU.subject_name = E.subject_name AND S.student_id = E.student_id
GROUP BY S.student_id, SU.subject_name
ORDER BY S.student_id, SU.subject_name;