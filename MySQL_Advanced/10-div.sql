-- a function thta divides the first by the second--
DELIMITER $$

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT DEFAULT 0;

    IF b != 0 THEN
        SET result = a /b;
END IF;
RETURN result;

END $$

DELIMITER;