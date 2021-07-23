/**
 */
package monitoringmm.impl;

import monitoringmm.*;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;

import org.eclipse.emf.ecore.impl.EFactoryImpl;

import org.eclipse.emf.ecore.plugin.EcorePlugin;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model <b>Factory</b>.
 * <!-- end-user-doc -->
 * @generated
 */
public class MonitoringmmFactoryImpl extends EFactoryImpl implements MonitoringmmFactory {
	/**
	 * Creates the default factory implementation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public static MonitoringmmFactory init() {
		try {
			MonitoringmmFactory theMonitoringmmFactory = (MonitoringmmFactory)EPackage.Registry.INSTANCE.getEFactory(MonitoringmmPackage.eNS_URI);
			if (theMonitoringmmFactory != null) {
				return theMonitoringmmFactory;
			}
		}
		catch (Exception exception) {
			EcorePlugin.INSTANCE.log(exception);
		}
		return new MonitoringmmFactoryImpl();
	}

	/**
	 * Creates an instance of the factory.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MonitoringmmFactoryImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EObject create(EClass eClass) {
		switch (eClass.getClassifierID()) {
			case MonitoringmmPackage.MO_AGENT: return createMOAgent();
			case MonitoringmmPackage.MO_CONFIG: return createMOConfig();
			case MonitoringmmPackage.MO_PROPERTY: return createMOProperty();
			case MonitoringmmPackage.MO_VALUE: return createMOValue();
			default:
				throw new IllegalArgumentException("The class '" + eClass.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MOAgent createMOAgent() {
		MOAgentImpl moAgent = new MOAgentImpl();
		return moAgent;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MOConfig createMOConfig() {
		MOConfigImpl moConfig = new MOConfigImpl();
		return moConfig;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MOProperty createMOProperty() {
		MOPropertyImpl moProperty = new MOPropertyImpl();
		return moProperty;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MOValue createMOValue() {
		MOValueImpl moValue = new MOValueImpl();
		return moValue;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MonitoringmmPackage getMonitoringmmPackage() {
		return (MonitoringmmPackage)getEPackage();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @deprecated
	 * @generated
	 */
	@Deprecated
	public static MonitoringmmPackage getPackage() {
		return MonitoringmmPackage.eINSTANCE;
	}

} //MonitoringmmFactoryImpl
