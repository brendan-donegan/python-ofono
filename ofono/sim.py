import dbus


SIM_MANAGER_INTERFACE = 'org.ofono.SimManager'

class SimManager:

    def __init__(self, sim_number=0):
        bus = dbus.SystemBus()
        modem = bus.get_object('org.ofono', '/ril_{}'.format(sim_number))
        self._manager = dbus.Interface(modem, SIM_MANAGER_INTERFACE)

    def is_pin_locked():
        """Check if the SIM is locked with a PIN.

        :returns: True if the SIM is locked with a PIN, otherwise False
        """
        locked = self._manager.GetProperties()['LockedPins']
        return 'pin' in locked

    def pin_lock(pin_type, pin):
        """Lock the SIM with a PIN.

        :param pin_type: The type of PIN to lock the SIM with, pin or pin2
        :param pin: The PIN with which to lock the SIM
        """
        if not self.is_pin_locked():
            self._manager.LockPin(pin_type, pin)

    def pin_unlock(pin_type, pin):
        """Remove the PIN lock from a SIM.

        :param pin_type: The type of PIN the SIM has been
        locked with, pin or pin2
        :param pin: The PIN with which to unlock the SIM
        """
        if self.is_pin_locked():
            self._manager.UnlockPin(pin_type, pin)
        
    def enter_pin(pin_type, pin):
        """Enter the PIN to allow a PIN locked SIM to be used.

        :param pin_type: The type of PIN the SIM is
        locked with, pin or pin2
        :param pin: The PIN to enter
        """
        self._manager.EnterPin(pin_type, pin)
