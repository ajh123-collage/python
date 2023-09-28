START
    SET stuff TO [1, 34532, 214, 12223321, 54534, 22]
    SET listOfLists TO []
    SET output TO []
    FUNCTION splitList(list)
        SET mid TO LEGNTH OF(list) / 2
        SET leftList TO stuff[0: mid]
        SET rightList TO stuff[mid: LENGTH OF(stuff)]
        RETURN leftList, rightList
    END-FUNCTION

    FUNCTION iterateLists(list)
        FOR i IN range(LENGTH OF(list)) DO
            SET newlist1 AND newlist2 to splitList(list)
            IF LENGTH OF(newlist1) IS 1 THEN
                ADD newlist1 TO listOfLists
            END-IF
            IF LENGTH OF(newlist1) IS 1 THEN
                ADD newlist2 TO listOfLists
            END-IF
            SET newlistA1 AND newlistA2 to splitList(newlist1)
            SET newlistB1 AND newlistB2 to splitList(newlist2)
            iterateLists(newlistA1)
            iterateLists(newlistA2)
            iterateLists(newlistB1)
            iterateLists(newlistB2)
        END-FOR
    END-FUNCTION

    iterateLists(stuff)

    FOR i IN range(LEGNTH OF(list)) DO
        SET left TO listOfLists[i]
        SET right TO listOfLists[i + 1]

        
    END-FOR
END