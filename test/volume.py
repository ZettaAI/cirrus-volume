import pytest

import cirrusvolume as cv
import provenancetools as pt


SOURCES = ['tracer annotation']
MOTIVATION = 'proper documentation is helpful'
PROCESS = pt.Process(
              'testing CirrusVolume',
              {'patience for humor': 6/10},
              pt.process.PythonGithubEnv('.'))


def test_creation(testcloudvolume):
    'Testing whether basic instantiation of a CirrusVolume works'
    cirrusvolume = cv.CloudVolume(testcloudvolume.cloudpath)
    assert type(cirrusvolume) == cv.precomputed.CirrusVolumePrecomputed


@pytest.fixture
def readvolume(testcloudvolume):
    return cv.CloudVolume(testcloudvolume.cloudpath)


@pytest.fixture
def readwritevolume(testcloudvolume):
    return cv.CloudVolume(testcloudvolume.cloudpath,
                          sources=SOURCES,
                          motivation=MOTIVATION,
                          process=PROCESS)


def test_writeblocking(readvolume):
    with pytest.raises(AssertionError):
        readvolume[0:10, 0:10, 0:10] = 0
