# Dashboard Access Guide

## Why `http://0.0.0.0:5000` Doesn't Work

**`0.0.0.0` is NOT a valid address to connect to!**

- `0.0.0.0` means "listen on all network interfaces" (server-side)
- You **cannot** use it in a browser URL
- It's only used when **starting** the server, not when **accessing** it

---

## ✅ Correct URLs to Use

### On the Same Computer (Local Access):

```
http://localhost:5000
```

**OR**

```
http://127.0.0.1:5000
```

Both work the same way - they connect to your own computer.

---

### From Another Device on Same Network:

1. **Find your Mac's IP address:**
   ```bash
   ifconfig | grep "inet " | grep -v 127.0.0.1
   ```
   
   Look for something like: `inet 192.168.1.XXX`

2. **Use that IP address:**
   ```
   http://192.168.1.XXX:5000
   ```
   (Replace XXX with your actual IP)

---

## Quick Test

### Check if Dashboard is Running:

```bash
# Check if something is using port 5000
lsof -ti:5000

# If you see a process ID, the dashboard is running
```

### Test Connection:

```bash
# Test if dashboard responds
curl http://localhost:5000/api/current

# Should return JSON data if working
```

---

## Common Issues

### Issue 1: "Connection Refused"

**Cause:** Dashboard not running

**Fix:**
```bash
cd climate_control
source venv/bin/activate
python3 main.py
```

Wait for: `"Dashboard available at http://0.0.0.0:5000"`

Then use: `http://localhost:5000` (NOT 0.0.0.0!)

---

### Issue 2: "This site can't be reached"

**Cause:** Wrong URL or firewall blocking

**Fix:**
- Use `localhost` or `127.0.0.1`, NOT `0.0.0.0`
- Check if system is running
- Check firewall settings

---

### Issue 3: Dashboard Shows "Disconnected"

**Cause:** WebSocket connection issue

**Fix:**
- Refresh the page (F5 or Cmd+R)
- Check browser console for errors
- Make sure system is still running

---

## Understanding the Addresses

| Address | Meaning | Use Case |
|---------|---------|----------|
| `0.0.0.0` | Listen on all interfaces | Server binding (in code) |
| `localhost` | Your own computer | Browser access (same machine) |
| `127.0.0.1` | Loopback address | Browser access (same machine) |
| `192.168.x.x` | Local network IP | Browser access (other devices) |

---

## Step-by-Step Access

1. **Start the system:**
   ```bash
   cd climate_control
   source venv/bin/activate
   python3 main.py
   ```

2. **Wait for this message:**
   ```
   Dashboard available at http://0.0.0.0:5000
   ```

3. **Open browser and go to:**
   ```
   http://localhost:5000
   ```
   **NOT** `http://0.0.0.0:5000` ❌

4. **Dashboard should load!**

---

## Summary

- ✅ **Use:** `http://localhost:5000`
- ❌ **Don't use:** `http://0.0.0.0:5000`

The message "Dashboard available at http://0.0.0.0:5000" just means the server is listening. You still need to use `localhost` or `127.0.0.1` to actually connect!

