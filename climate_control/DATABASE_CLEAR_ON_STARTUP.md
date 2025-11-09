# Database Auto-Clear on Startup

## ✅ What Changed

The system now **automatically clears the database** every time you start it!

**No more old data persisting between sessions!**

---

## 🎯 How It Works

### On Every Startup:

1. System starts
2. DataLogger initializes
3. **Checks setting:** `LOGGING_CLEAR_ON_STARTUP`
4. **If True:** Clears all data from database
5. **Logs:** Shows how many records were deleted
6. Continues with fresh start

### What Gets Cleared:

- ✅ All sensor readings
- ✅ All control decisions
- ✅ All actuator states
- ✅ All system events

**Tables are kept** (structure preserved), only **data is deleted**.

---

## ⚙️ Configuration

### Current Setting (Development Mode):

**File:** `settings.py` line 74

```python
LOGGING_CLEAR_ON_STARTUP = True     # Clear database on startup (for development)
```

**Status:** ✅ **ENABLED** (clears on every startup)

---

## 🔧 How to Change

### To Keep Data (Production Mode):

Edit `settings.py`:

```python
LOGGING_CLEAR_ON_STARTUP = False    # Keep historical data
```

**Result:**
- Database persists between sessions
- Historical data preserved
- Good for production/deployment

### To Clear Data (Development Mode):

Edit `settings.py`:

```python
LOGGING_CLEAR_ON_STARTUP = True     # Clear on startup
```

**Result:**
- Fresh start every time
- No old data cluttering graphs
- Good for development/testing

---

## 📊 What You'll See

### On Startup (with clearing enabled):

```
INFO:data_logger:Database initialized at climate_data.db
INFO:data_logger:🗑️  Cleared database on startup: 150 readings, 45 decisions, 12 events removed
INFO:data_logger:   (This is enabled for development - set LOGGING_CLEAR_ON_STARTUP = False to keep data)
INFO:__main__:✓ Data logger initialized
```

### On Startup (with clearing disabled):

```
INFO:data_logger:Database initialized at climate_data.db
INFO:__main__:✓ Data logger initialized
```

---

## 🎓 Use Cases

### Development (Clear on Startup = True):

- ✅ Fresh start every session
- ✅ Clean graphs without old data
- ✅ Easier testing
- ✅ No manual cleanup needed

### Production (Clear on Startup = False):

- ✅ Historical data preserved
- ✅ Long-term trend analysis
- ✅ System performance tracking
- ✅ Data export capabilities

---

## 🔄 Manual Clear (If Needed)

If you want to clear data manually without restarting:

```bash
cd climate_control
source venv/bin/activate
python3 clear_old_data.py
```

Or delete the database file:

```bash
rm climate_control/climate_data.db
```

---

## 📝 Summary

| Setting | Behavior |
|---------|----------|
| `LOGGING_CLEAR_ON_STARTUP = True` | Database cleared on every startup (development) |
| `LOGGING_CLEAR_ON_STARTUP = False` | Database persists between sessions (production) |

**Current setting:** `True` (clears on startup)

**To change:** Edit `settings.py` line 74

---

## 🚀 Next Steps

1. **Restart your system** - Database will be cleared automatically!
2. **Check logs** - You'll see the clear message
3. **View dashboard** - Should show clean, fresh data
4. **For production** - Set `LOGGING_CLEAR_ON_STARTUP = False`

**Enjoy your fresh start every time!** 🎉

