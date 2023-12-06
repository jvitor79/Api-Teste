# Entities

## Movie

- id: integer
- title: varchar(128)
- duration: integer
- category: varchar(128)
- score: integer

## Series

- id: integer
- title: varchar(128) (foreign key season.series_title)
- seasons: integer

## Season

- id: integer
- season_number: integer (foreign key episodes.season)
- series_title: varchar(128) (foreign key series.title)
- title: varchar(128)

## Episode

- ep_number: integer
- title: varchar(128)
- season: integer (foreign key seasons.season)
- score: integer
