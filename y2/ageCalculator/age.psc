START
    INPUT petType
    INPUT petAge

    SET realAge TO 0
    IF petType IS "cat" THEN
        SET i to 0
        IF i LESS THAN petAge THEN
            IF i LESS THAN 2 THEN
                SET realAge TO realAge + 25
            ELSE
                SET realAge TO realAge + 4
            END-IF
        END-IF
    ELSE IF petType IS "dog" THEN
        SET realAge TO petAge * 4
    END-IF
    OUTPUT realAge
END
