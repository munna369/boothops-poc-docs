# Setup

This document contains the configuration details for the BoothOps POC Supabase project.

## Supabase Configuration

| Key | Value |
|-----|-------|
| **Project URL** | `https://ihkqgppfdvhxvyivdvoy.supabase.co` |
| **Anon Key** | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imloa3FncHBmZHZoeHZ5aXZkdm95Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzMzczODgsImV4cCI6MjA5MzkxMzM4OH0.GVCUbcWT41gICwvgyAeGg2th-JCYRYnH0ENziyYZ5hs` |

## Usage

Use these values to initialize the Supabase client in your application:

```js
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://ihkqgppfdvhxvyivdvoy.supabase.co'
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imloa3FncHBmZHZoeHZ5aXZkdm95Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzMzczODgsImV4cCI6MjA5MzkxMzM4OH0.GVCUbcWT41gICwvgyAeGg2th-JCYRYnH0ENziyYZ5hs'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)
```

> **Note:** The anon key is safe to use in the browser when Row Level Security (RLS) is enabled on your tables.
