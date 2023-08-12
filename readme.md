# wodr

wordlist generator for offline brute force attacks

## usage
1) Add custom entries in the resources files
2) `bash wodr.sh > wordlist.txt`

## password common patterns

- {Word}{Number}
- {Word}{Symbol}{Number}
- {Word}{Number}{Symbol}
- {Word}
- {Number}

### Word

{Word} usually is:

1. Special Names: The name/nickname of the own user or someone he loved, like "john", "alex", "bia".
2. Company Names: The name of the company that developed the app, such as "Microsoft", "MS", "Micro", "Soft".
3. Favorite word: Some crazy word that the user enjoys or messed with his head, such as "Pikachu", "God", "Vina".

### Number

{Number} usually is:

1. Sequential Numbers: Sequences like "123", "321" or "55555" are commonly used by people to create passwords.
2. Repeating Digits: Patterns like "000", "333" or "111111" are straightforward to remember but weak as passwords.
3. Lucky Numbers: Some individuals use numbers they consider lucky, like "777", "888" or "1010" as part of their passwords.
4. Year Patterns: People often incorporate years with special significance to them or recent years into their passwords, such as "1990", "2000" or "2021".
5. Birthdays: Many people use their own or their loved ones' birthdates as part of their passwords. For example, "05121985", "04032016" or "0308John".

