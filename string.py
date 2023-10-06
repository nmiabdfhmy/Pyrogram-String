from pyrogram import Client

API_ID = input("Enter your API_ID : ")
API_HASH = input("Enter your API_HASH : ")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, in_memory=True)

string_session = ""

async def main():
    async with app:
        string_session = await app.export_session_string()
        info = await app.get_me()
        fname = info.first_name
        await app.send_message("me", f"PYROGRAM STRING\n\nString Session :\n\n`{string_session}`\n\n☕Powered by @RedflixHD")
        print(f"\nSuccessfully Logged in as {fname}\n\nCheck your Saved Messagae to get your String.\n\n")

app.run(main())