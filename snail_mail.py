# "hello.worldcom"    => An email address has to contain a '@' character!
# "he@llo@world.com"  => An email address cannot contain more than one '@' characters!
# "@world.com"        => The username before the '@' character cannot be empty!
# "hello@"            => The domain after the '@' character cannot be empty!
# "hello@worldcom"    => An email address has to contain at least one '.' character!
# "hell.o@worldcom"   => The domain has to contain at least one '.' character!
# "he.llo@worldcom."  => The top-level domain cannot be empty!
# "he.llo@worldco.m"  => The top-level domain has to be at least two characters long!
# ".hello@world.com"  => The username cannot start with a '.' character!
# "he.llo@.world.com" => The domain cannot start with a '.' character!
# "hello@world.com"   => Valid email address :)


def email_validator(email):

    length_of_email = len(email)
    number_of_at_characters = email.count("@")
    number_of_dot_characters = email.count(".")
    position_of_at = email.find("@")

    position_of_first_dot = email.find(".")
    position_of_last_dot = email.rfind(".")
    position_of_first_dot_after_the_at = -1 # Initial value is -1, means not found
    if position_of_at != -1:  # if '@' exists 
        position_of_first_dot_after_the_at = email.find(".", position_of_at) # this looks for the first '.' after '@'
        


    error_message_no_at = "An email address has to contain a '@' character!"
    error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
    error_message_no_dot = "An email address has to contain at least one '.' character!"
    error_message_no_username = "The username before the '@' character cannot be empty!"
    error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
    error_message_no_server_name = "The domain cannot start with a '.' character!"
    error_message_no_tld = "The top-level domain cannot be empty!"
    error_message_short_tld = "The top-level domain has to be at least two characters long!"
    error_message_no_domain = "The domain after the '@' character cannot be empty!"
    error_message_invalid_username = "The username cannot start with a '.' character!"

    ok_message = "Valid email address :)"
    is_valid = True


    # 1. At least one '@'
    if number_of_at_characters == 0:
        print(error_message_no_at)
        is_valid = False

    # 2. Only one '@'
    if number_of_at_characters > 1:
        print(error_message_too_many_at)
        is_valid = False

    # 3. Username is not empty
    if position_of_at == 0:
        print(error_message_no_username)
        is_valid = False

    # 4. Domain cannot be empty
    if position_of_at == length_of_email - 1:
        print(error_message_no_domain)
        is_valid = False

    # 5. At least one '.' character
    if number_of_dot_characters == 0:
        print(error_message_no_dot)
        is_valid = False
    
    # 6. At least one '.' in domain
    if position_of_first_dot_after_the_at == 0:
        print(error_message_no_dot_in_domain)
        is_valid = False

    # 7. Top-level domain is not empty
    if position_of_last_dot == length_of_email - 1:
        print(error_message_no_tld)
        is_valid = False

    # 8. TLD is at least two characters long
    if (length_of_email - position_of_last_dot - 1) < 2:
        print(error_message_short_tld)
        is_valid = False

    # 9. Valid username
    if email.startswith("."):
        print(error_message_invalid_username)
        is_valid = False

    # 10. Valid server name
    if position_of_at + 1 == ".":
        print(error_message_no_server_name)
        is_valid = False

    # 11. Everything is in order :)
    if is_valid:
        print(ok_message)

while True:
    email_addr = input("Please enter an e-mail-address: ")
    email_validator(email_addr)