SELECT *
FROM FOOD_PRODUCT
WHERE price = (SELECT MAX(price)
              FROM FOOD_PRODUCT)