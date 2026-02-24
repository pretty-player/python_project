messages = [
    "Hello everyone",
    "Buy cheap products",
    "This is spam",
    "More spam",
    "SPAM isn't present here",
    "Buy valid products",
    "ADMIN: Please behave"
]

def moderate_chat(message_list):
    # Create an iterator from the list
    msg_iterator = iter(message_list)
    approved_messages = []

    print("--- 🛡️ Starting Message Moderation ---")

    while True:
        try:
            # Get the next message from the iterator
            msg = next(msg_iterator)
            
            # Conversion to lowercase for robust filtering
            lower_msg = msg.lower()
            
            # Check if 'spam' or 'admin' is in the message
            if "spam" not in lower_msg and "admin" not in lower_msg:
                approved_messages.append(msg)
            else:
                print(f"[REJECTED]: {msg}")

        except StopIteration:
            # This error is raised when the iterator has no more items
            break

    return approved_messages

# Execute moderation
final_list = moderate_chat(messages)

print("\n" + "="*30)
print(f"Approved Messages: {final_list}")