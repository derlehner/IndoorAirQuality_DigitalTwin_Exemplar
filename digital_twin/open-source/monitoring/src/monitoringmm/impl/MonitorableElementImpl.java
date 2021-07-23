/**
 */
package monitoringmm.impl;

import monitoringmm.MonitorableElement;
import monitoringmm.MonitoringmmPackage;

import org.eclipse.emf.common.notify.Notification;

import org.eclipse.emf.ecore.EClass;

import org.eclipse.emf.ecore.impl.ENotificationImpl;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Monitorable Element</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link monitoringmm.impl.MonitorableElementImpl#getTopic <em>Topic</em>}</li>
 *   <li>{@link monitoringmm.impl.MonitorableElementImpl#isSync <em>Sync</em>}</li>
 * </ul>
 *
 * @generated
 */
public abstract class MonitorableElementImpl extends NamedElementImpl implements MonitorableElement {
	/**
	 * The default value of the '{@link #getTopic() <em>Topic</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getTopic()
	 * @generated
	 * @ordered
	 */
	protected static final String TOPIC_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getTopic() <em>Topic</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getTopic()
	 * @generated
	 * @ordered
	 */
	protected String topic = TOPIC_EDEFAULT;

	/**
	 * The default value of the '{@link #isSync() <em>Sync</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #isSync()
	 * @generated
	 * @ordered
	 */
	protected static final boolean SYNC_EDEFAULT = false;

	/**
	 * The cached value of the '{@link #isSync() <em>Sync</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #isSync()
	 * @generated
	 * @ordered
	 */
	protected boolean sync = SYNC_EDEFAULT;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected MonitorableElementImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return MonitoringmmPackage.Literals.MONITORABLE_ELEMENT;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public String getTopic() {
		return topic;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setTopic(String newTopic) {
		String oldTopic = topic;
		topic = newTopic;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, MonitoringmmPackage.MONITORABLE_ELEMENT__TOPIC, oldTopic, topic));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public boolean isSync() {
		return sync;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setSync(boolean newSync) {
		boolean oldSync = sync;
		sync = newSync;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, MonitoringmmPackage.MONITORABLE_ELEMENT__SYNC, oldSync, sync));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case MonitoringmmPackage.MONITORABLE_ELEMENT__TOPIC:
				return getTopic();
			case MonitoringmmPackage.MONITORABLE_ELEMENT__SYNC:
				return isSync();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case MonitoringmmPackage.MONITORABLE_ELEMENT__TOPIC:
				setTopic((String)newValue);
				return;
			case MonitoringmmPackage.MONITORABLE_ELEMENT__SYNC:
				setSync((Boolean)newValue);
				return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
			case MonitoringmmPackage.MONITORABLE_ELEMENT__TOPIC:
				setTopic(TOPIC_EDEFAULT);
				return;
			case MonitoringmmPackage.MONITORABLE_ELEMENT__SYNC:
				setSync(SYNC_EDEFAULT);
				return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
			case MonitoringmmPackage.MONITORABLE_ELEMENT__TOPIC:
				return TOPIC_EDEFAULT == null ? topic != null : !TOPIC_EDEFAULT.equals(topic);
			case MonitoringmmPackage.MONITORABLE_ELEMENT__SYNC:
				return sync != SYNC_EDEFAULT;
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String toString() {
		if (eIsProxy()) return super.toString();

		StringBuilder result = new StringBuilder(super.toString());
		result.append(" (topic: ");
		result.append(topic);
		result.append(", sync: ");
		result.append(sync);
		result.append(')');
		return result.toString();
	}

} //MonitorableElementImpl
