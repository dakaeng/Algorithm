-- 코드를 입력하세요
SELECT MCDP_CD AS 진료과코드, COUNT(APNT_NO) AS 5월예약건수
FROM APPOINTMENT
WHERE APNT_YMD BETWEEN '2022-05-01' AND '2022-05-31'
GROUP BY 진료과코드
ORDER BY 5월예약건수, 진료과코드;