from va_profile_opt_in_out_lambda import va_profile_opt_in_out_lambda_handler
from sqlalchemy import text

#create test database#

COUNT = r"""SELECT COUNT(*) FROM va_profile_local_cache;"""

OPT_IN_OUT = text("""SELECT va_profile_opt_in_out(:va_profile_id, :communication_item_id, :communication_channel_id, :allowed, :source_datetime);""")

def test_va_profile_cache_exists(notify_db):
    assert notify_db.engine.has_table("va_profile_local_cache")

#create function returning dictionary#

def create_bios_element(tx_audit_id: str, source_date: str, va_profile_id: int, communication_channel_id: int, communication_item_id: int, is_allowed: bool) -> dict:
    return {
        "txAuditId": tx_audit_id,
        "sourceDate": source_date,
        "vaProfileId": va_profile_id,
        "communicationChannelId": communication_channel_id,
        "communicationItemId": communication_item_id,
        "allowed": is_allowed,
    }

def create_event(tx_audit_id: str, source_date: str, va_profile_id: int, communication_channel_id: int, communication_item_id: int, is_allowed: bool) -> dict:
    return {
        "bios": [
            create_bios_element(tx_audit_id, source_date, va_profile_id, communication_channel_id, communication_item_id, is_allowed)
        ]
    }

#assert test#

def test_communication_channel_id_not_5():
    event = create_event("tx_audit_id", "2022-04-27T16:57:16Z", 2, 3, 4, True)
    response = va_profile_opt_in_out_lambda_handler(event)
    assert isinstance(response, dict), "response is not a dictionary"