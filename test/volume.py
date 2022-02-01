import pytest

import cirrusvolume as cv
import provenancetoolbox as ptb


SOURCES = ['tracer annotation']
MOTIVATION = 'proper documentation is helpful'
PROCESS = ptb.Process(
              'testing CirrusVolume',
              {'patience for humor': 6/10},
              ptb.PythonGithubEnv('.'))


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
