![Go Version](https://img.shields.io/badge/Go-1.19+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

# Gator - RSS Feed Aggregator
cat > README.md << 'EOF'
# Gator - RSS Feed Aggregator

A powerful command-line RSS feed aggregator built with Go and PostgreSQL. Collect, follow, and browse content from your favorite RSS feeds all in one place.

## Features

- 🔐 **User Management** - Register, login, and manage multiple users
- 📰 **Feed Management** - Add, list, and organize RSS feeds
- 🔄 **Feed Following** - Follow/unfollow feeds and see what you're subscribed to
- 🤖 **Automatic Aggregation** - Continuously fetch new posts in the background
- 📖 **Post Browsing** - Browse latest posts from all your followed feeds
- 💾 **PostgreSQL Backend** - Robust data storage with proper relationships

## Prerequisites

- **Go 1.19+** - [Install Go](https://golang.org/doc/install)
- **PostgreSQL 12+** - [Install PostgreSQL](https://www.postgresql.org/download/)

## Installation

### Using Go Install

```bash
go install github.com/ad4-commits/blog_aggregator@latest
