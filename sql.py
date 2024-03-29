#Задание №1
SELECT c.login,
       COUNT(o."courierId")
FROM "Couriers" AS c INNER JOIN "Orders" AS o ON c.id=o."courierId"
WHERE o."InDelivery"=true
GROUP BY c.login;

#Задание №2

SELECT track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "InDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders";
