# skysecure_assignemnt
AI-Powered Zoho Project Chatbot for skysecure assignment.
## Environment Configuration (.env)

Create a `.env` file in the root directory:

```
ZOHO_CLIENT_ID=your_client_id
ZOHO_CLIENT_SECRET=your_client_secret
ZOHO_REDIRECT_URI=http://localhost:8000/auth/callback
ZOHO_ACCOUNTS_URL=https://accounts.zoho.com

SESSION_SECRET=your_secret_key
```

---

## OAuth Configuration Guide (Zoho)

1. Go to Zoho Developer Console
2. Create a **Server-based Application**
3. Set Redirect URI:

   ```
   http://localhost:8000/auth/callback
   ```
4. Copy:

   * Client ID
   * Client Secret
5. Add them to the `.env` file
