# shuffle

Simple (and restricted) *Python* method to shuffle and enumerate files inside a directory.

The files in a given directory are randomly shuffled and enumerated either using 2 or 3 digits, depending on how many files are inside the directory.

In case there are less than 100 files, the enumeration prefix will consist of 2 digits, e.g.

```ruby
01 Foo
02 Bar
03 Example
...
74 And
81 So
92 On
...
```

and in case there are 100 files and more (up to 999), the prefix consists of 3 digits. However, in case there are more than 999 files, there will be a 2-digit prefix again (which might cause problems) as there is no handler for more files than 999.

The method to shuffle and enumerate is a quick-and-dirty solution for a simple MP3 shuffle tool I wrote for a good friend of mine. For details the `shuffle_mp3_example.py` (please read the comments inside the file before using it, as it not actually is a tool itself).

Anyway, the `shuffle_enum` method requires the `random` and `shutil` *Python* modules in order to work.

## Usage

Notice that the source file names will not be changed in any way. The processed files will be copied into the given target directory.

```python
shuffle_enum(dir_source,        # source directory containing the files to process
             dir_target,        # destination directory for the processed files
             action="shuffle")  # action to perform, options see below
```

Possible actions are:

* `shuffle`
  * Shuffle and enumerate files (by adding leading numbers).
* `reshuffle`
  * Shuffle and enumerate already shuffled files again.
* `remove`
  * Remove leading numbers.

For example, if you want to shuffle and enumerate all files inside `/home/johndoe/music` and copy the processed files to `/home/johndoe/music_shuffled` (the directory alrady must exist, of course) it would look like this

```python
phrasegen(dir_source="/home/johndoe/music", dir_target="/home/johndoe/music_shuffled", action="shuffle")
```

or in the short form:

```python
phrasegen("/home/johndoe/music", "/home/johndoe/music_shuffled", action="shuffle")
```
