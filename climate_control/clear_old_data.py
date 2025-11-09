#!/usr/bin/env python3
"""
Quick script to clear old database data.
Use this to remove old simulated data (e.g., from when base_temp was 5°C)
so you can see clean, stable new data.
"""

import os
import sys
from data_logger import DataLogger
from settings import get_config_dict

def clear_all_data():
    """Clear all data from the database."""
    config = get_config_dict()
    db_path = config.get('logging', {}).get('database_path', 'climate_data.db')
    
    if not os.path.exists(db_path):
        print(f"Database {db_path} does not exist. Nothing to clear.")
        return
    
    print(f"Clearing all data from {db_path}...")
    
    try:
        logger = DataLogger(config)
        
        # Get count before clearing
        import sqlite3
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM sensor_readings")
        readings_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM control_decisions")
        decisions_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM system_events")
        events_count = cursor.fetchone()[0]
        
        conn.close()
        
        print(f"Found: {readings_count} readings, {decisions_count} decisions, {events_count} events")
        
        # Clear all data
        logger.cleanup_old_data(days=0)  # 0 days = delete everything
        
        logger.close()
        
        print("✅ All data cleared successfully!")
        print("   Restart your system to start collecting new, stable data.")
        
    except Exception as e:
        print(f"❌ Error clearing data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("=" * 60)
    print("Clear Old Database Data")
    print("=" * 60)
    print()
    
    response = input("This will delete ALL data from the database. Continue? (yes/no): ")
    
    if response.lower() in ['yes', 'y']:
        clear_all_data()
    else:
        print("Cancelled.")

