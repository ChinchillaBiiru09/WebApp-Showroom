# ========================================================================
# CAR QUERY - START ======================================================
# ========================================================================
CAR_ADD_QUERY = """
    INSERT INTO apps_car (brand, model, year, price, description, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
"""
CAR_GET_ALL_QUERY = """
    SELECT * FROM apps_car
    WHERE is_deleted = 0
"""
CAR_GET_JOIN_BY_ID_QUERY = """
    SELECT * FROM apps_car
    INNER JOIN apps_service 
    ON apps_car.id = apps_service.car_id
    WHERE apps_car.id = %s AND apps_car.is_deleted = 0
"""
CAR_GET_BY_ID_QUERY = """
    SELECT * FROM apps_car
    WHERE id = %s AND is_deleted = 0
"""
CAR_DELETE_QUERY = """
    UPDATE apps_car
    SET is_deleted = 1, deleted_at = NOW()
    WHERE id = %s
"""
# ========================================================================
# CAR QUERY - END ========================================================
# ========================================================================


# ========================================================================
# CAR QUERY - START ======================================================
# ========================================================================
LOAN_ADD_QUERY = """
    INSERT INTO apps_loan (car_id, loan, interest_rate, created_at, updated_at)
    VALUES (%s, %s, %s, NOW(), NOW())
"""
LOAN_GET_BY_CAR_QUERY = """
    SELECT * FROM apps_loan
    WHERE car_id = %s AND is_deleted = 0
"""
# ========================================================================
# CAR QUERY - END ========================================================
# ========================================================================


# ========================================================================
# SERVICE QUERY - START ==================================================
# ========================================================================
SERVICE_ADD_QUERY = """
    INSERT INTO apps_service (car_id, price, description, created_at, updated_at)
    VALUES (%s, %s, %s, NOW(), NOW())
"""
SERVICE_GET_ALL_QUERY = """
    SELECT * FROM apps_service
    WHERE is_deleted = 0
"""
SERVICE_GET_BY_CAR_QUERY = """
    SELECT * FROM apps_service
    WHERE car_id = %s AND is_deleted = 0
"""
# ========================================================================
# SERVICE QUERY - END ====================================================
# ========================================================================