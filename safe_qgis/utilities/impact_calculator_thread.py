"""
InaSAFE Disaster risk assessment tool developed by AusAid -
**ISImpactCalculatorThread.**

The module provides a high level interface for running SAFE scenarios.

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'tim@linfiniti.com, ole.moller.nielsen@gmail.com'
__date__ = '11/01/2011'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import threading
import traceback
import sys
import logging

from PyQt4.QtCore import (QObject,
                          pyqtSignal)

from safe_qgis.safe_interface import calculateSafeImpact
from safe_qgis.exceptions import InsufficientParametersError

LOGGER = logging.getLogger('InaSAFE')


class ImpactCalculatorThread(threading.Thread, QObject):
    """A threaded class to compute an impact scenario.

        Under python a thread can only be run once, so the instances
        based on this class are designed to be short lived.

        We inherit from QObject so that we can use Qt translation self.tr
        calls and emit signals.

       .. todo:: implement this class using QThread as a base class since it
          supports thread termination which python threading doesnt seem to do.
          Also see the techbase article below for emitting signals across
          threads using Qt.QueuedConnection.
          http://techbase.kde.org/Development/Tutorials/
          Python_introduction_to_signals_and_slots

       Users of this of this class can listen for signals indicating
       when processing is done. For example::

         from is_impact_calculator_thread import ImpactCalculatorThread
         n = ImpactCalculatorThread()
         n.done.connect(n.showMessage)
         n.done.emit()

       Prints 'hello' to the console

       .. seealso::
          http://techbase.kde.org/Development/Tutorials/
          Python_introduction_to_signals_and_slots

          for an alternative (maybe nicer?) approach.
    """
    done = pyqtSignal()

    def show_message(self):
        """For testing only"""
        print 'hello'

    def __init__(self, hazard_layer, exposure_layer, function):
        """Constructor for the impact calculator thread.

        :param hazard_layer: read_layer object containing the Hazard.
            data.
        :type hazard_layer: read_layer

        :param exposure_layer: read_layer object containing the Exposure data.
        :type exposure_layer: read_layer

        :param function: Function that defines how the Hazard assessment
            will be computed.
        :type function: FunctionProvider

        :raises: InsufficientParametersError if not all parameters are set.
        """
        threading.Thread.__init__(self)
        QObject.__init__(self)
        self._hazardLayer = hazard_layer
        self._exposureLayer = exposure_layer
        self._function = function
        self._impactLayer = None
        self._result = None
        self._exception = None
        self._traceback = None

    def impact_layer(self):
        """Get the impact output from the last run.

        :returns: An impact layer.
        :rtype: read_layer
        """
        return self._impactLayer

    def result(self):
        """Return the result of the last run.

        :returns: A message containing the status info for the last run.
        :rtype: str
        """
        return self._result

    def lastException(self):
        """Get any exception that may have been raised while running.

        :returns: An exception if any.
        :rtype: Exception
        """
        return self._exception

    def last_traceback(self):
        """Get the stack trace for any exception occurring in the last run."""
        return self._traceback

    def run(self):
        """ Main function for hazard impact calculation thread.

        Requires three properties to be set before execution
        can take place:

        * Hazard layer - a path to a raster,
        * Exposure layer - a path to a vector points layer.
        * Function - a function that defines how the Hazard assessment
          will be computed.

        After the thread is complete, you can use the filename and
        result accessors to determine what the result of the analysis was::

          calculator = ImpactCalculator()
          rasterPath = os.path.join(TESTDATA, 'xxx.asc')
          vectorPath = os.path.join(TESTDATA, 'xxx.shp')
          calculator.setHazardLayer(self.rasterPath)
          calculator.setExposureLayer(self.vectorPath)
          calculator.setFunction('Flood Building Impact Function')
          myRunner = calculator.getRunner()
          #wait till completion
          myRunner.join()
          myResult = myRunner.result()
          myFilename = myRunner.filename()


        :raises: InsufficientParametersError

        .. note:: a done signal is emitted when the analysis is complete.
        """
        if (self._hazardLayer is None) or \
                (self._exposureLayer is None) or \
                (self._function is None):
            myMessage = self.tr(
                'Ensure that hazard, exposure and function are all set before '
                'trying to run the analysis.')
            raise InsufficientParametersError(myMessage)
        try:
            myLayers = [self._hazardLayer, self._exposureLayer]
            self._impactLayer = calculateSafeImpact(
                theLayers=myLayers, theFunction=self._function)
        except MemoryError, e:
            myMessage = self.tr(
                'An error occurred because it appears that your system does '
                'not have sufficient memory. Upgrading your computer so that '
                'it has more memory may help. Alternatively, consider using a '
                'smaller geographical area for your analysis, or using '
                'rasters with a larger cell size.')
            self._exception = e
            self._traceback = traceback.format_tb(sys.exc_info()[2])
            self._result = myMessage
            LOGGER.exception(myMessage)
        # Catch and handle all other exceptions:
        # pylint: disable=W0703
        except Exception, e:
            myMessage = self.tr('Calculation error encountered:\n')
            #store the exception so that controller class can get it later
            self._exception = e
            self._traceback = traceback.format_tb(sys.exc_info()[2])
            self._result = myMessage
            LOGGER.exception(myMessage)
        else:
            self._result = self.tr('Calculation completed successfully.')
        # pylint: enable=W0703

        #  Let any listening slots know we are done
        # noinspection PyUnresolvedReferences
        self.done.emit()
