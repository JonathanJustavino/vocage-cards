# vocage-cards

Repository storing the words for Vocabulary Trainer [Vocage](https://github.com/proycon/vocage)

## Usage

`vocage --help` provides a full overview of the parameters available

## Quickstart

*Prerequisite:* Data in TSV format has to be available

```zsh
vocage data.tsv
```

## Key Bindings

space / enter - 'Flip' the card, shows the next side (i.e. the solution)
Arrow down / `j` - Keep card on the same deck and go to the next card (usually a random card unless you are in ordered mode)
PageDown / `J` - Skip the card (it may be presented again immediately in the same session) and go to the next card (a random card will be selected)
Arrow up / `k` - Skip this card for now and go to the previous card
Arrow right / `l` - Promote this card to the next deck
Arrow left / `h` - Promote this card to the previous deck
A number key - Move the card to the n'th deck
`w` - Save progress (input files will be amended)
`q` - Quit (asks for confirmation is you have unsaved changes)
`Q` - Quit (without saving, don't ask confirmation)
`a` - Toggle between showing all cards and showing only cards that are due (default) (`--all`)
`s` - Toggle between presenting unseen cards (default) and showing only cards that have been presented before. (`--seen`)
`z` - Toggle between ordered mode and random mode (default) (--ordered). In ordered mode, cards will be presented in the order they are defined.
