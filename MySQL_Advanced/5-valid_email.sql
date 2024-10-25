-- a reseting trigger --
CREATE TRIGGER new_email BEFORE UPDATE ON users
FOR EACH ROW IF OLD.email != NEW.email THEN
	SET NEW.valid_email = 0;
    END IF;