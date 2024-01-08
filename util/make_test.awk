#!/usr/bin/awk -f

BEGIN{
    {FS="[ (]"}
    {print "import pytest"}
    {print "from unittest.mock import Mock, patch"}
    {print "\n"}
}

/def/ {print "def test_"$2"():\n\tpass"}
END{
}
