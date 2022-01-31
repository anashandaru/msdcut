from obspy import read
from obspy.core import UTCDateTime
from os.path import basename
import click

def readStreamList(filename):
    result = []
    for item in filename:
        result.append(read(item))
    return result

def getStartEnd(streamList):
    starttimeList = []
    endtimeList = []
    for stream in streamList:
        for trace in stream:
            starttimeList.append(trace.stats.starttime)
            endtimeList.append(trace.stats.endtime)
    start = max(starttimeList)
    end = min(endtimeList)
    return [start, end]

def write2file(stream, filename):
    stream.write(filename, format="MSEED")

@click.command()
@click.argument('filename', type=click.Path(exists=True),nargs=-1)
def main(filename):
    stream = readStreamList(filename)
    minStart, maxEnd = getStartEnd(stream)
    minStart = str(minStart)[:19]
    maxEnd = str(maxEnd)[:19]
    start = click.prompt('Starttime [min/example= {} ]'.format(minStart), type=str)
    end = click.prompt('Endtime [max/example= {} ]'.format((maxEnd)), type=str)
    start = UTCDateTime(start)
    end = UTCDateTime(end)
    for i, item in enumerate(stream):
        item.trim(start, end)
        write2file(item, "cut-"+basename(filename[i]))
    click.echo("File is cutted")
 
if __name__ == '__main__':
    main()