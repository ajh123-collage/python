START
    SET stock TO {}

    FUNCTION login()
        INPUT username
        INPUT password
        IF username EQUAL TO "bob" THEN
            IF password EQUAL TO "qwerty123" THEN
                menu()
                RETURN
            END-IF
        END-IF
        login()
    END-FUNCTION

    FUNCTION menu()
        OUTPUT "1. Set stock"
        OUTPUT "2. Add stock"
        OUTPUT "3. Remove stock"
        OUTPUT "4. Exit"
        INPUT choice
        IF choice EQUAL TO 1 THEN
            setStock()
        ELSE-IF choice EQUAL TO 2 THEN
            addStock()
        ELSE-IF choice EQUAL TO 3 THEN
            removeStock()
        ELSE-IF choice EQUAL TO 4 THEN
            RETURN
        END-IF
    END-FUNCTION

    FUNCTION setStock()
        INPUT itemName
        INPUT itemAmount
        IF itemAmount < 1 THEN
            OUTPUT "Amount cannot be less than 1"
            setStock()
        ELSE
            SET stock[itemName] TO itemAmount
            OUTPUT "Item added"
        END
    END-FUNCTION

    FUNCTION addStock()
        INPUT itemName
        INPUT itemAmount

        IF stock[itemName] IS EMPTY THEN
            OUTPUT "Item does not exist
            addStock()
        ELSE
            SET realAmount TO stock[itemName]
            SET stock[itemName] TO realAmount + itemAmount
            OUTPUT "Item(s) Added"
        END
    END-FUNCTION

    FUNCTION removeStock()
        INPUT itemName
        INPUT itemAmount

        IF stock[itemName] IS LESS THAN itemAmount THEN
            SET realAmount TO stock[itemName]
            SET stock[itemName] TO realAmount - itemAmount
            OUTPUT "Item(s) removed"
        ELSE
            OUTPUT "Not enougth items"
            removeStock()
        END
    END-FUNCTION

    login()
END