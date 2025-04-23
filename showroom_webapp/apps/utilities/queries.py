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
CAR_GET_BY_ID_QUERY = """
    SELECT * FROM apps_car
    WHERE id = %s AND is_deleted = 0
"""
CAR_UPDATE_QUERY = """
    UPDATE apps_car
    SET brand = %s, model = %s, year = %s, price = %s, 
    description = %s, updated_at = NOW() 
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
# SERVICE QUERY - START ======================================================
# ========================================================================
SERVICE_ADD_QUERY = """
    INSERT INTO apps_service (car_id, price, description, created_at, updated_at)
    VALUES (%s, %s, %s, NOW(), NOW())
"""
SERVICE_GET_ALL_QUERY = """
    SELECT * FROM apps_service
    WHERE is_deleted = 0
"""
SERVICE_GET_BY_ID_QUERY = """
    SELECT * FROM apps_service
    WHERE id = %s AND is_deleted = 0
"""
SERVICE_UPDATE_QUERY = """
    UPDATE apps_service
    SET brand = %s, model = %s, year = %s, price = %s, 
    description = %s, updated_at = NOW() 
    WHERE id = %s AND is_deleted = 0
"""
SERVICE_DELETE_QUERY = """
    UPDATE apps_service
    SET is_deleted = 1, deleted_at = NOW()
    WHERE id = %s
"""
# ========================================================================
# SERVICE QUERY - END ========================================================
# ========================================================================