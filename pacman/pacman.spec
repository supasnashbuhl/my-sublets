# -*- encoding: utf-8 -*-
# Pacman specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Pacman"
  s.version     = "0.2"
  s.tags        = [ ]
  s.files       = [ "pacman.rb" ]
  s.icons       = [ "pacman.xbm" ]

  # Sublet description
  s.description = "Display pacman available updates"
  s.notes       = <<NOTES
Show updates available in Archs pacman package manager
Needs this: https://gist.github.com/952010 run as a cronjob
NOTES

  # Sublet authors
  s.authors     = [ "crshd, Joakim Reinert" ]
  s.contact     = "crshd@mail.com or mail@jreinert.com"
  s.date        = "Thu May 23 11:58:12 CEST 2013"

  # Sublet config
  s.config = [
    {
      :name        => "interval",
      :type        => "integer",
      :description => "Update interval",
      :def_value   => "3600"
    },
    {
      :name        => "separator",
      :type        => "string",
      :description => "String to seperate repos",
      :def_value   => " // "
    },
    {
      :name        => "updatefile",
      :type        => "string",
      :description => "File that holds pacman update info",
      :def_value   => "#{ENV['HOME']}/.pacmanupdates"
    },
    {
      :name        => "repositories",
      :type        => "hash",
      :description => "Hash containing the repositories that are displayed (with labels as values)",
      :def_value   => '"core" => "!:", "extra" => "e:", "community" => "c:"'
    }
  ]

  # Sublet grabs
  #s.grabs = {
  #  :PacmanGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end