from curses import echo
from email.mime import base
from obspy import read
from obspy.core import UTCDateTime
from os.path import basename
import click


def getStartEnd(st):
    return [st[0].stats.starttime, st[0].stats.endtime]

def write2file(stream, filename):
    stream.write(filename, format="MSEED

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    stream = read(filename)
    minStart, maxEnd = getStartEnd(stream)
    minStart = str(minStart)[:19]
    maxEnd = str(maxEnd)[:19]
    start = click.prompt('Starttime [min/example= {} ]'.format(minStart), type=str)
    end = click.prompt('Endtime [max/example= {} ]'.format((maxEnd)), type=str)
    start = UTCDateTime(start)
    end = UTCDateTime(end)
    stream.trim(start, end)
    write2file(stream, "cut-"+basename(filename))
    click.echo("File is cutted")
 
if __name__ == '__main__':
    main()